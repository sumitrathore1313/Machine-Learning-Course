
"""FACE DETECTION: Draws squares around detected faces in the given image."""

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw


api_key_path = "apikey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=api_key_path


def detect_face(face_file):
    
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations

def highlight_faces(image, faces, output_filename):

    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    # Sepecify the font-family and the font-size
    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

    im.save(output_filename)


def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image)

        print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, output_filename)
# [END vision_face_detection_tutorial_run_application]


if __name__ == '__main__':
    input_image = "test/IMG_8355-1-800x600.jpg"
    output = "test/output_face.jpg"
    main(input_image, output, 4)
