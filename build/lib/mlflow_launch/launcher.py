import os
import platform
import subprocess


def start_mlflow_server(
    backend_store_uri="sqlite:///J:/JConner/sqlite/mlflow.db",
    default_artifact_root="file:///J:/JConner/sqlite/mlruns",
    port=5000,
    host="127.0.0.1",
    env_name="NIR-prod-mlflow",
    window_title="[mlflow-server]",
    package_manager="mamba",
):
    """
    Opens a new terminal window and starts the MLflow tracking server.

    This function is primarily designed for Windows and uses the 'start'
    command to launch a new, separate command prompt. It can be easily
    adapted for macOS or Linux.

    Args:
        backend_store_uri (str): The URI for the backend store.
        default_artifact_root (str): The default artifact root for experiments.
        port (int): The port to run the server on.
        host (str): The host to bind the server to.
        env_name (str): The name of the conda/mamba environment to use.
        window_title (str): The title for the new terminal window (Windows only).
        package_manager (str): The package manager to use ('conda' or 'mamba').
    """
    # Construct the core mlflow server command with all its arguments.
    mlflow_command = (
        f"mlflow server "
        f'--backend-store-uri "{backend_store_uri}" '
        f'--default-artifact-root "{default_artifact_root}" '
        f"--port {port} "
        f"--host {host}"
    )

    # Use 'conda run' which is the modern, recommended way to execute a command
    # within a specific conda environment without needing to activate it first.
    command_to_run_in_env = f"{package_manager} run -n {env_name} {mlflow_command}"

    print(
        f"Preparing to execute command in the '{env_name}' environment using '{package_manager}'..."
    )

    try:
        # Check the operating system to use the correct command for opening a new terminal.
        if platform.system() == "Windows":
            # On Windows, the 'start' command opens a new window.
            # The first quoted string is the title of the new window.
            # 'cmd /K' ensures the window stays open to show server logs.
            full_command = f'start "{window_title}" cmd /K "{command_to_run_in_env}"'
            print(f"Executing for Windows: {full_command}")
            os.system(full_command)

        else:  # Linux
            # For Linux, this is a common command for gnome-terminal.
            # It might need to be adjusted for other terminal emulators like xterm or konsole.
            # The '--' separates terminal options from the command to be run.
            # 'exec bash' keeps the terminal open if the script exits.
            linux_command = [
                "gnome-terminal",
                "--",
                "bash",
                "-c",
                f"{command_to_run_in_env}; exec bash",
            ]
            print(f"Executing for Linux: {' '.join(linux_command)}")
            subprocess.Popen(linux_command)

        print("\n✅ Successfully launched a new terminal to start the MLflow server.")
        print(f"   The server should be available shortly at http://{host}:{port}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("   Please ensure that:")
        print(
            f"   1. The conda environment '{env_name}' exists and has MLflow installed."
        )
        print("   2. The 'conda' command is available in your system's PATH.")
        print(
            "   3. Your terminal application (Terminal, gnome-terminal) is installed and accessible."
        )
