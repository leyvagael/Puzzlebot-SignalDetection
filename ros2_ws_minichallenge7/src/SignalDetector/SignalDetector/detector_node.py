import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO
import json
import cv2

class DetectorNode(Node):
    def __init__(self):
        super().__init__('SignalDetector')
        
        # Carga el modelo - ajusta la ruta a donde tengas tu best.pt
        self.model = YOLO('/home/skqchs/Documents/Sexto/Challenge7/my_model/my_model.pt')
        self.bridge = CvBridge()
        
        # Suscripción a la cámara
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.image_callback,
            10
        )
        
        # Publicación de resultados
        self.publisher = self.create_publisher(String, '/detecciones', 10)
        
        self.get_logger().info('Nodo detector iniciado correctamente')

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        results = self.model(frame, verbose=False)

        detecciones = []
        for r in results:
            for box in r.boxes:
                clase = self.model.names[int(box.cls)]
                confianza = round(float(box.conf), 2)
                x1, y1, x2, y2 = [int(v) for v in box.xyxy[0].tolist()]

                detecciones.append({
                    'clase': clase,
                    'confianza': confianza,
                    'bbox': [x1, y1, x2, y2]
                })

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                etiqueta = f'{clase} {confianza}'
                cv2.putText(frame, etiqueta, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Detector de Señales', frame)
        cv2.waitKey(1)

        self.publisher.publish(String(data=json.dumps(detecciones)))

        if detecciones:
            self.get_logger().info(f'Detectado: {[d["clase"] for d in detecciones]}')

'''
    def image_callback(self, msg):
        # Convertir imagen ROS → OpenCV
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # Correr inferencia
        results = self.model(frame, verbose=False)
        
        # Parsear resultados
        detecciones = []
        for r in results:
            for box in r.boxes:
                detecciones.append({
                    'clase': self.model.names[int(box.cls)],
                    'confianza': round(float(box.conf), 2),
                    'bbox': box.xyxy[0].tolist()
                })
        
        # Publicar
        self.publisher.publish(String(data=json.dumps(detecciones)))
        
        if detecciones:
            self.get_logger().info(f'Detectado: {[d["clase"] for d in detecciones]}')
'''

def main(args=None):
    rclpy.init(args=args)
    node = DetectorNode()
    rclpy.spin(node)
    rclpy.shutdown()
