# Tennessee Tech Research Day, April 2023

## Neural Network for Determining the Minimum Number of Turns Required to Solve a Rubik's Cube

### By Jacob Gable

Below are instructions for how to generate a dataset, train the model, and run the model.

## Generating the dataset

To generate a dataset, use the following command:

```bash
python format_data.py data/10000.txt ds.txt
```

Replace `data/10000.txt` with a text file containing your data. I have 6 text files,

```text
1.txt
5.txt
100.txt
3800.txt
6200.txt
100000.txt
```

`1.txt` has 1 entry, `5.txt` has 2 entries, etc.

Replace `ds.txt` with the name of the output file. Whatever you want it to be.

## Training the model

To train the model, run the following command:

```bash
python model.py ds.txt new
```

`ds.txt` is the name of your data file.

This will also automatically run the model.

## Running the model

To run the model without training it, run the following command:

```bash
python model.py ds.txt
```
