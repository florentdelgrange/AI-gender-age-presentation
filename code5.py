img = load_img('gandalf.png',
    target_size=(299, 299))
x = img_to_array(img)
x = np.array(x, dtype='uint8')
show(x)
print("age : {} "
    .format(model.predict
        (preprocess_input(np.array([x])))))
