output "api_id" {
  value = aws_api_gateway_rest_api.api.id
}

output "lambda_env_table_name" {
  value = aws_lambda_function.api.environment[0].variables.TABLE_NAME
}
