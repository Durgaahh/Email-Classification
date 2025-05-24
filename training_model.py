if __name__ == "__main__":
    import data_loader
    import preprocessing
    import vectorizer
    from train_models import encode_labels, train_models, save_model
    
    df = data_loader.load_sms_dataset()
    df = preprocessing.preprocess_dataframe(df)
    vectorizer_obj, X = vectorizer.create_vectorizer_and_transform(df)
    y = encode_labels(df)

    model = train_models(X, y)
    save_model(model)
    vectorizer.save_vectorizer(vectorizer_obj)
    print("Model and vectorizer saved successfully.")
