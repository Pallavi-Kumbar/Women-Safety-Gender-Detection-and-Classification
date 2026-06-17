import cv2
import numpy as np
import tensorflow as tf

from safety_analyzer import calculate_safety

model = tf.keras.models.load_model(
    "models/gender_model.h5"
)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_detector.detectMultiScale(
        gray,
        1.3,
        5
    )

    male_count = 0
    female_count = 0

    for (x,y,w,h) in faces:

        face = frame[y:y+h,x:x+w]

        face = cv2.resize(
            face,
            (128,128)
        )

        face = face/255.0

        face = np.expand_dims(
            face,
            axis=0
        )

        prediction = model.predict(
            face,
            verbose=0
        )

        confidence = float(prediction[0][0])

        if confidence > 0.5:

            label = f"Female {confidence:.2f}"

            female_count += 1

            color = (0,255,0)

        else:

            label = f"Male {(1-confidence):.2f}"

            male_count += 1

            color = (255,0,0)

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            color,
            2
        )

        cv2.putText(
            frame,
            label,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    danger,status = calculate_safety(
        male_count,
        female_count
    )

    cv2.putText(
        frame,
        f"Male: {male_count}",
        (10,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,0,0),
        2
    )

    cv2.putText(
        frame,
        f"Female: {female_count}",
        (10,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Danger Score: {danger}",
        (10,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,0,255),
        2
    )

    cv2.putText(
        frame,
        status,
        (10,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,0,255),
        2
    )

    if danger > 80:

        cv2.imwrite(
            "alerts/high_risk.jpg",
            frame
        )

    cv2.imshow(
        "Women Safety Analysis",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()