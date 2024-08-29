## Model Architecture
![]()


* In AWS Lambda an older version of `boto3` is present. Make sure to install the latest version of `boto3` or any required python packages using the following steps

1. Create a folder `python` in your local.
2. In your terminal run: `pip install <package_name> -t python/`
3. After all the required package folders have been created, convert the `python` folder to a zip file. For example,`boto3_layer.zip`
4. To create a layer ``Create layer > Name the layer > Upload the zip file> Select the Python runtime version > Click Create
5. Go to AWS Lambda, scroll to `Layers > Add layer > Custom layers > Select your newly created layer in the above step > Select a version > Add`

### Creating API Gateway
This API will trigger the Lambda function and generate a response
1. Select `API Gateway > APIs > Create API > HTTP API > Create an API > <Your API name> > Create`
2. Adding routes `Click Create`
  * POST `blog_generation_api > Attach intergration > Choose Lambda function > Create` - now lambda function has been integrated
3. Creating Stages - required for testing purposes
  * `Go to project folder > Deploy > Stages > Create > Dev_env > Deploy`


### Create a S3 bucket 
* Create a S3 bucket with a unique_nname

-- Setup pf the project is done.

### Testing the project

1. Open POST request > API_Gateway_URL_stage/ROUTE
  * For example: `https://aws.kdldvddf/dev/blog_generation`
2. In Postman body > raw,
`
{
   "blog_topic" : "Generative AI use cases in Marketing Tech"
}
`
3. All the results can be viewed in S3 bucket



### Monitoring
- All the logs can be viewed in AWS CloudWatch

