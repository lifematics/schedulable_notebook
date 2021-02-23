# Schedulable notebook

This application is based on [jupyter-with-jenkins](https://github.com/yacchin1205/jupyter-with-jenkins)

After Jupyter Notebook is open, you can open the Jenkins UI from the `jenkins` menu.

![jenkins button](images/jenkins.png)

## Running notebook periodically

You can use [papermill](https://github.com/nteract/papermill) to let Jenkins execute your notebook.


```
# Move notebook directory
cd /home/jovyan/

# Execute notebook
papermill "Using Selenium.ipynb" "${WORKSPACE}/${BUILD_ID}.ipynb"
```

