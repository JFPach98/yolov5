# YOLOv5 Custom Model

Pasos:

1. Crear ambiente virtual
2. Instalar pytorch 1.7 y cuda 1.0.1
```
pip install torch==1.7.0+cu101 torchvision==0.8.1+cu101 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```

3. Clonar repositorio y descargar dependencias:

```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
cd ..
```

4. Descomprimir las carpetas de labels y de imágenes.

```
unzip labels
unzip dataset
```

- Si se cuenta con las imágenes de forma local, se puede crear una carpeta 'dataset' y se pueden insertar las imagenes en esta. Se puede hacer, de igual manera, para las labels.
- Las labels tienen que estar en formato yolo darknet. Para convertir a este formato, se puede correr este script:

```
convert_labels.py
```

5. Crear carpetas de test y de train, crear para cada carpeta subcarpetas de images y labels:
```
mkdir data
cd data
mkdir train,test
cd train
mkdir images,labels
cd ..
cd test
mkdir images,labels
cd ../..
```

6. Correr setup.py para crear datasets de entrenamiento y de prueba.

 ```
 python setup.py
 ```

7. Mover archivos 'classes.yaml' y 'yolov5.pt:

 ```
 mv classes.yaml ./yolov5
 mv yolov5.pt ./yolov5
 ```

8. Para entrenar de cero, utilizando los pesos de yolov5, se corre el siguiente script:
 
 ```
 cd yolov5
 python train.py --img 640 --batch 8 --epochs 30 --data classes.yaml --cfg ./yolov5/models/yolov5s.yaml --weights 'yolov5.pt' --name custom_model
 ```

- Nótese que 'custom_model' es el nombre con el que se guardan los pesos. 

- Si se desea correr con un archivo de pesos ya entrenados (archivo .pt), se corre el siguiente script, en weights se introduce la ruta del script:

```
python train_mod.py --img 640 --batch 8 --epochs 30 --data ../data/classes.yaml --cfg yolov5s.yaml --weights custom_model.pt --name yolov5s_ternium2 --nosave --cache
```

9. Para hacer la identificación de objetos, se corre el script detect.py usando los siguientes parámetros:
```
python detect.py --weights weights/custom_model.pt --img 640 --conf 0.4 --source 
```

- Delante de source se introduce el path a las imágenes a procesar por el modelo.
