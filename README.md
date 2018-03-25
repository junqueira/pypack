# py-pack  

Generate package egg, that can be attached to Spark clusters in production or included in a PySpark console.

$ python=3.6.1

### Install dependences
	pip install -r requirements.txt

### Create module pypack
	python setup.py install

### Test solutions 
	python tests/test_mission.py 

### Command line to Generate package egg, your code in a dist/pypack-0.0.1-py3.6.egg 
	python setup.py bdist_egg

### Start the PySpark console and attach the egg file.
	pyspark --py-files dist/pypack-0.0.1-py3.6.egg


### From the PySpark REPL, you can import the pypack code and execute the application code.

+ from pypack.spark import *
+ from pypack.mission import with_life_goal
+ source_data = [ ("jose", 1), ("pedro", 2) ]
+ source_df = spark.createDataFrame( source_data, ["name", "age"])
+ actual_df = with_life_goal(source_df)
+ actual_df.show()



### The pypack library can be attached to spark-submit commands for launching applications in a similar manner.
