# Chess Board to Array Converter (Chess AI coming soon !)

This Python script converts a chess board to a numpy array for use in machine learning models. It uses the Stockfish chess engine to generate game and to generate win% and black% of winning.

## How to Use

1. Install the required libraries by running `pip install chess numpy`.
2. Download the Stockfish chess engine and update the path in the code. You can download it [here](https://stockfishchess.org/download/).
3. Run the script it will generate 2 file : x_train and y_train wich will both are stored using the pickle module

## Example

The eval.py file is an example on how to fetch the games and evaluation that are in x_train and y_train

## Note

- This does not include testing data so be carefull around that !

- I used the lichess.org formula to get win and lose %. Thanks to them
## Dependencies

- `chess`: Python Chess Library
- `numpy`: Numerical Python Library
- `Stockfish` : The Best Chess Engine at the time

## Author

- GitHub: [seb-link](https://github.com/seb-link)
