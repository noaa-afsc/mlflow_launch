Launches mlflow server from Python script or notebook. Defaults are for FT-NIRS MMCNN model tracking.

```Python
from mlflow_launch import start_mlflow_server

start_mlflow_server(backend_store_uri="sqlite:///J:/JConner/sqlite/mlflow.db", default_artifact_root="file:///J:/JConner/sqlite/mlruns", package_manager="mamba")
