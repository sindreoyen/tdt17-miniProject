
## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment:**
    ```sh
    python3 -m venv .env
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        .env\Scripts\Activate.ps1
        ```
    - On macOS/Linux:
        ```sh
        source .env/bin/activate
        ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Jupyter notebook:**

The Jupyter notebook can be ran by setting up the virtual environment as explained above, and selecting the correct kernel in the `.ipynb` file under `src`. It can also be ran via the terminal CLI with

    ```sh
    jupyter notebook src/pole_detection.ipynb
    ```

2. **Follow the instructions in the notebook to perform pole detection.**

## Data

- Redistribution of the used dataset is prohibited but is available under `/cluster/projects/vc/data/ad/open/Poles` on the NTNU Idun cluster.

## Acknowledgements

- NTNU's NAPLab for the collection and annotation of the LiDAR image dataset that has been used for model development in this project.