# mlflow_launcher/__main__.py

import argparse
from .launcher import start_mlflow_server


def main():
    """Main function to run the MLflow server launcher from the command line."""
    parser = argparse.ArgumentParser(
        description="Launch the MLflow tracking server in a new terminal window."
    )

    parser.add_argument(
        "--backend-store-uri",
        default="sqlite:///G:/My Drive/Projects/FT-NIR Production/model_tracking_db/sqlite//mlflow.db",
        help="The URI for the backend store.",
    )
    parser.add_argument(
        "--default-artifact-root",
        default="file:///G:/My Drive/Projects/FT-NIR Production/model_tracking_db/sqlite/mlruns",
        help="The default artifact root for experiments.",
    )
    parser.add_argument(
        "--port", type=int, default=5000, help="The port to run the server on."
    )
    parser.add_argument(
        "--host", default="127.0.0.1", help="The host to bind the server to."
    )
    parser.add_argument(
        "--env-name",
        default="NIR-prod-mlflow",
        help="The name of the conda/mamba environment to use.",
    )
    parser.add_argument(
        "--package-manager",
        default="conda",
        choices=["conda", "mamba"],
        help="The package manager to use ('conda' or 'mamba').",
    )

    args = parser.parse_args()

    start_mlflow_server(
        backend_store_uri=args.backend_store_uri,
        default_artifact_root=args.default_artifact_root,
        port=args.port,
        host=args.host,
        env_name=args.env_name,
        package_manager=args.package_manager,
    )


if __name__ == "__main__":
    main()
