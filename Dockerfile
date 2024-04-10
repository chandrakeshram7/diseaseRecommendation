FROM tensorflow/serving

# Set the working directory
WORKDIR /models

# Copy your exported TensorFlow model from S3 into the container
COPY s3://mymlmodel1/plant_disease_prediction_model.h5 /models/plant_disease_prediction_model.h5

# Expose the gRPC and HTTP ports
EXPOSE 8500
EXPOSE 8501

# Start TensorFlow Serving when the container starts
CMD ["tensorflow_model_server", "--rest_api_port=8501", "--model_name=plant_disease_prediction_model", "--model_base_path=/models"]
