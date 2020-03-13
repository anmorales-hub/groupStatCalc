<h1>Outline</h1>
<h2>Stats Calulator</h2>

1. <h3>Math Operations</h3>

    * __Addition__
    * __Subtraction__    
    * __Multiplication__
    * __Division__
    * __Exponent__
    * __Root__
    * __Log__
    
2. <h3> Random Number Generator (RNG)</h3>

    * __Random Integer__
        * Specified seed
        * No specified seed
    * **Random Float**
        * Specified seed
        * No specified seed
    * **Random list of *n* integers (specified seed)**
    * **Random list of *n* floats (specified seed)**
    * **Randomly select an item from a list**
        * Specified seed
        * No specified seed
    * **Randomly select *n* number of items from a list**
        * Specified seed
        * No specified seed
        
3. <h3>Descriptive Statistic Functions</h3>

     * **Mean**
         * import mean from numpy
     * **Median**
         * import median from statistics
     * **Mode**
         * import mode from statistics
     * **Mode Deviation**
         * calls mean method from Mean class
         * import absolute function from numpy
     * **Population Proportion**
         * calls on listPickListSeed method from ListPick class (to obtain sample data)
     * **Standard Deviation**
         * import stdev from statistics
     * **Covariance**
         * import cov from numpy
     * **Population Correlation**
         * import stddev method from Stddev class (standard deviation)
         * import covariance method from Covariance class    
     * **Sample Correlation**
         * import listPickListSeed from ListPick class (to obtain sample data)
         * import stddev method from Stddev class (standard deviation)
         * import covariance method from Covariance class
     * **Quartiles (First, Second, Third)**
         * import percentile function from numpy
     * **Variance**
         * import variance from numpy
     * **Skewness**
         * import skew from scipy

4. <h3> Population Sampling </h3>

     * **Simple Random Sample**
         * import listPickListSeed from ListPick class - generates random sample from data set
     * **Systematic Sample**
         * import listPickListSeed from ListPick class
     * **Margin of Error**
         * import zsc from Zsc class (z-score)
         * import stddev from Stddev class (standard deviation)
     * **Confidence Interval (Population)**
         * import sem and t from scipy.stats
         * import mean from Mean class
     * **Confidence Interval (Sample)** 
         * import simpRandSamp from SimpRandSamp class (simple random sample)
         * import confidenceIntervalPopulation from ConfidenceIntervalPopulation class
     * **Cochran Sample Size Formula**
         * import zsc from Zsc class (z-score)
         * import marginOfError from MarginOfError class
         * import exponent and subraction from MathOperations
         * import populationProportion from PopulationProportion class
     * **Sample Size with conf. interval and width (no pop. std dev)**
         * import exponent, division, and subtraction from MathOperations
         * import zsc from Zsc class (z-score)
         * import marginOfError from Margin of Error class
      * **Sample Size with conf. interval and width (known pop. std dev)**
         * import exponent from MathOperations
         * import zsc from Zsc class (z-score)
         * import marginOfError from Margin of Error class
         * import stddev from Stddev class (standard deviation)
         
     
