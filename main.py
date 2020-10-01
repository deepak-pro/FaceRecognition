import face_recognition

#You may need a lot of images to train them first.

billGatesPicture = face_recognition.load_image_file("bill.jpg")
billFaceEncoding = face_recognition.face_encodings(billGatesPicture)[0]

unknownPicture = face_recognition.load_image_file("unknown.jpg")
unknownFaceEncoding = face_recognition.face_encodings(unknownPicture)[0]

results = face_recognition.compare_faces([billFaceEncoding],unknownFaceEncoding)

if results[0] == True:
    print("Unknown Picture is of Bill Gates")
else:
    print("Unknown Picture is not of Bill Gates")

