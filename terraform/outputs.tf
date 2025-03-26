output "api_id" {
  value = aws_api_gateway_rest_api.api.id
}

output "lambda_env_table_name" {
  value = aws_lambda_function.api.environment_variables["TABLE_NAME"]
}
