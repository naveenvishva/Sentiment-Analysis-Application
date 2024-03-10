### Sentiment Analysis Application

This project entails building a sentiment analysis application using a pre-trained model and a graphical user interface (GUI) developed with PyQt5. The Python scripts included are `sentiment_model.py`, which contains the sentiment prediction model, and `sentiment_gui.py`, which contains the GUI for user interaction.

### Files Included:

- `sentiment_model.py`: Python script for sentiment prediction using a pre-trained model.
- `sentiment_gui.py`: Python script for the PyQt5 GUI application for sentiment analysis.
- `sentiment_model.h5`: Pre-trained sentiment prediction model saved in the HDF5 format.
- `data.json`: JSON file containing text data for configuring the tokenizer.

### Prerequisites:

Ensure you have Python installed on your system along with the required libraries. You can install necessary packages using pip.

### Usage:

1. **Running the Application**:
   - Run `sentiment_gui.py` to launch the GUI application.
   - Enter a review in the input field and click "Analyze" to predict its sentiment.
   - Click "View Analysis" to visualize the sentiment distribution of all reviews entered.

### Note:
- Ensure the provided `sentiment_model.h5` and `data.json` files are present in the same directory as the scripts.
- The sentiment prediction model has been pre-trained and is loaded from `sentiment_model.h5`.
- The tokenizer configuration is loaded from `data.json` to preprocess input text.

### References:
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [TensorFlow Documentation](https://www.tensorflow.org/guide)
- [NLTK Documentation](https://www.nltk.org/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
