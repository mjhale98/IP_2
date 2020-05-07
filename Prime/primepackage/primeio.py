#primeio.py
import csv
def write_primes(l, file_name):
        """Writes the contents of a list to a new, one-row CSV file. It takes a list l and a string file_name,
        and will raise an IOError if the file can't be created.  """
        try:
                with open(file_name, "w", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(l)
        except IOError as argument:
                print("Can't create file!", argument)
        else:
                print("Succesfully written file!")
        finally:
                print("End of write_primes")
     
                
 
def read_primes(file_name):
        """Reads a csv file, writes the contents to a list, and returns the list. Takes a string file_name. Will throw an IOError if the file can't be read."""
        primeList = []
        try:
                with open(file_name, "r") as f:
                        reader = csv.reader(f)
                        for row in reader:
                                primeList.append(row)
                        return primeList
        except IOError as argument:
                print("Can't read this file!", argument)
        else:
                print("File succesfully read!")
        finally:
                print("End of read_primes")
                
