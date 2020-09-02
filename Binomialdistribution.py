import math
import matplotlib.pyplot as plt
from Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
    
       
    def __init__(self, p=0.5, n=100):
        self.p = p
        self.n = n

        Distribution.__init__(self, mu=self.calculate_mean(), sigma=self.calculate_stdev()) 
        
    
    def calculate_mean(self): 
        """Function to calculate the mean from p and n

        Args: 
            None

        Returns: 
            float: mean of the data set

        """
        self.mean = self.p * self.n
        return self.mean




    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
   
        """
        
        self.n = len(self.data)
        self.p = self.data.count(1) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n
    # TODO: write a method plot_bar() that outputs a bar chart of the data set according to the following specifications.
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
    def plot_bar(self):
        
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        possible_outcomes = [1,0]
        ocurrences = [self.data.count(x) for x in possible_outcomes]
        ax.bar(possible_outcomes, ocurrences)
        plt.show()
        
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
            Rigorously, this should have been called a probability mass function.
            
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        #probability of one specific outcome with k successes
        specific_probability = math.pow(self.p, k) * math.pow(1 - self.p, self.n - k)
        
        possible_combinations = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k))
        
        return specific_probability * possible_combinations
    # write a method to plot the probability density function of the binomial distribution
    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """


        
        fig = plt.figure()
        ax = plt.add_axes([0, 0, 1, 1])
        k_list = range(self.n + 1)
        mass_list = [self.pdf(k) for k in k_list]
        plt.bar(k_list, mass_list)
        plt.show()
        
        
    def __add__(self, other):   
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        

        return Binomial(p=self.p, n=self.n+other.n)
    
    def __repr__(self):
        
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """

        return f"mean {self.mean}, standard deviation {self.stdev}, p{self.p}, n {self.n}"

    
        
