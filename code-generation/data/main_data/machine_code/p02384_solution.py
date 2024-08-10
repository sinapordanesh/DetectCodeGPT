def dice_II(faces, num_questions, questions):
    right_side_faces = []
    for question in questions:
        top_face, front_face = question
        if top_face == faces[0]:
            if front_face == faces[1]:
                right_side_faces.append(faces[2])
            elif front_face == faces[2]:
                right_side_faces.append(faces[4])
            elif front_face == faces[3]:
                right_side_faces.append(faces[1])
            elif front_face == faces[4]:
                right_side_faces.append(faces[3])
        elif top_face == faces[1]:
            if front_face == faces[0]:
                right_side_faces.append(faces[3])
            elif front_face == faces[2]:
                right_side_faces.append(faces[0])
            elif front_face == faces[3]:
                right_side_faces.append(faces[5])
            elif front_face == faces[5]:
                right_side_faces.append(faces[2])
        elif top_face == faces[2]:
            if front_face == faces[0]:
                right_side_faces.append(faces[1])
            elif front_face == faces[1]:
                right_side_faces.append(faces[5])
            elif front_face == faces[4]:
                right_side_faces.append(faces[0])
            elif front_face == faces[5]:
                right_side_faces.append(faces[4])
        elif top_face == faces[3]:
            if front_face == faces[0]:
                right_side_faces.append(faces[4])
            elif front_face == faces[1]:
                right_side_faces.append(faces[0])
            elif front_face == faces[4]:
                right_side_faces.append(faces[5])
            elif front_face == faces[5]:
                right_side_faces.append(faces[1])
        elif top_face == faces[4]:
            if front_face == faces[0]:
                right_side_faces.append(faces[2])
            elif front_face == faces[2]:
                right_side_faces.append(faces[5])
            elif front_face == faces[3]:
                right_side_faces.append(faces[1])
            elif front_face == faces[5]:
                right_side_faces.append(faces[3])
        elif top_face == faces[5]:
            if front_face == faces[1]:
                right_side_faces.append(faces[3])
            elif front_face == faces[2]:
                right_side_faces.append(faces[1])
            elif front_face == faces[3]:
                right_side_faces.append(faces[4])
            elif front_face == faces[4]:
                right_side_faces.append(faces[2])
    return right_side_faces

faces = [1, 2, 3, 4, 5, 6]
num_questions = 3
questions = [(6, 5), (1, 3), (3, 2)]

output = dice_II(faces, num_questions, questions)
for o in output:
    print(o)