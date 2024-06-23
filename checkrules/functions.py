import re
from .log import msg


def IsVersionTag(tag:str) -> bool:
    version_pattern = re.compile(r'^[a-zA-Z0-9_-]*:?(\d+\.\d+(\.\d+)?(-rc)?)([a-zA-Z0-9._-]*)?$')
    match = version_pattern.match(tag)
    return match is not None

def SecretKeys() -> list:
    return [
        "FASTLY_API_TOKEN", "AWS_CLOUDFRONT_DISTRIBUTION_ID", "AWS_CLOUDFRONT_ACCESS_ID",
        "PINTEREST_API_SECRET", "QUICKBOOKS_CONSUMER_KEY", "QUICKBOOKS_CONSUMER_SECRET",
        "SENDINBLUE_API_KEY", "TWILIO_VERIFY_SERVICE_SID", "TWILIO_FLEX_ACCOUNT_SID",
        "BRAIN_TREE_MERCHANT_ID", "BRAIN_TREE_PUBLIC_KEY", "BRAIN_TREE_PRIVATE_KEY",
        "DB_NAME", "STRIPE_SECRET_KEY", "PAYPAL_CLIENT_ID", "PAYPAL_CLIENT_SECRET",
        "SAP_CLIENT_SECRET", "SERVICE_NOW_CLIENT_ID", "SERVICE_NOW_CLIENT_SECRET",
        "RABBITMQ_HOST", "RABBITMQ_USERNAME", "RABBITMQ_PASSWORD", "SESSION_ID",
        "KUBERNETES_API_KEY", "KUBERNETES_SECRET_TOKEN", "KIBANA_ACCESS_TOKEN",
        "PAYPAL_WEBHOOK_SECRET", "STRIPE_PUBLISHABLE_KEY", "STRIPE_SECRET_KEY",
        "WEATHERSTACK_ACCESS_KEY", "STORMGLASS_API_KEY", "MAPBOX_ACCESS_TOKEN",
        "INSTAGRAM_CLIENT_ID", "INSTAGRAM_CLIENT_SECRET", "PINTEREST_API_KEY",
        "CLOUDFLARE_API_TOKEN", "CLOUDFLARE_ACCOUNT_ID", "CLOUDFLARE_ZONE_ID",
        "TYPEFORM_API_KEY", "SURVEYMONKEY_API_KEY", "SURVEYMONKEY_API_SECRET",
        "TAX_CALCULATION_API_KEY", "ZAPIER_API_KEY", "ZAPIER_WEBHOOK_SECRET",
        "BITRISE_API_KEY", "BITRISE_BUILD_SECRET", "DOCKER_HUB_ACCESS_TOKEN",
        "LAMBDA_ACCESS_POLICY_ARN", "SES_SMTP_USERNAME", "SES_SMTP_PASSWORD",
        "REDIS_URL", "REDIS_PASSWORD", "SENTRY_DSN", "NEW_RELIC_LICENSE_KEY",
        "WORDPRESS_API_KEY", "WORDPRESS_API_SECRET", "SALESFORCE_CLIENT_ID",
        "FRESHDESK_API_KEY", "NOTION_INTEGRATION_TOKEN", "MIXPANEL_API_KEY",
        "FIREBASE_API_KEY", "FIREBASE_DATABASE_URL", "FIREBASE_AUTH_DOMAIN",
        "TIKTOK_ACCESS_TOKEN", "TIKTOK_REFRESH_TOKEN", "PINBOARD_API_TOKEN",
        "AUTH0_CLIENT_SECRET", "SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET",
        "SPOTINST_API_TOKEN", "ALGOLIA_ADMIN_API_KEY", "LAMBDA_SECRET_KEY",
        "SENDINBLUE_SMTP_KEY", "WEATHER_API_KEY", "EMAIL_PROVIDER_API_KEY",
        "AWS_CLOUDFRONT_SECRET_KEY", "NOTION_SECRET", "NOTION_DATABASE_ID",
        "AZURE_CLIENT_SECRET", "AZURE_TENANT_ID", "AZURE_SUBSCRIPTION_ID",
        "NETLIFY_ACCESS_TOKEN", "CONTENTFUL_ACCESS_TOKEN", "GHOST_API_KEY",
        "OAUTH_CLIENT_ID", "OAUTH_CLIENT_SECRET", "GOOGLE_OAUTH_CLIENT_ID",
        "MONGO_DB_PASSWORD", "ELASTICSEARCH_URL", "ELASTICSEARCH_USERNAME",
        "SALESFORCE_CLIENT_SECRET", "AMPLITUDE_API_KEY", "HUBSPOT_API_KEY",
        "DROPBOX_API_KEY", "TWILIO_PHONE_NUMBER", "INTERCOM_ACCESS_TOKEN",
        "SERVERLESS_ACCESS_KEY", "STELLAR_SECRET_KEY", "SHIPPING_API_KEY",
        "DIGITALOCEAN_ACCESS_TOKEN", "APIFY_API_TOKEN", "TOMTOM_API_KEY",
        "ROCKETCHAT_API_KEY", "ROCKETCHAT_SECRET", "MATTERMOST_API_KEY",
        "AWS_SECRET_ACCESS_KEY", "MY_TOKEN", "APP_TOKEN", "VAULT_TOKEN",
        "APP_ENV", "APP_DEBUG", "APP_URL", "APP_NAME", "STRIPE_API_KEY",
        "PIVOTAL_TRACKER_API_KEY", "JIRA_API_KEY", "JIRA_CLIENT_SECRET",
        "GITLAB_ACCESS_TOKEN", "GITLAB_PRIVATE_TOKEN", "ATLAS_API_KEY",
        "DYNAMODB_ACCESS_KEY", "DYNAMODB_SECRET_KEY", "REDIS_ENDPOINT",
        "AUTHY_API_KEY", "ONESIGNAL_APP_ID", "ONESIGNAL_REST_API_KEY",
        "ZENDESK_API_KEY", "SALESFORCE_ACCESS_TOKEN", "SAP_CLIENT_ID",
        "TIDAL_CLIENT_ID", "TIDAL_CLIENT_SECRET", "PAYPAL_WEBHOOK_ID",
        "SENDGRID_API_KEY", "MANDRILL_API_KEY", "LAMBDA_FUNCTION_ARN",
        "ADOBE_CLIENT_SECRET", "OKTA_CLIENT_ID", "OKTA_CLIENT_SECRET",
        "WEBFLOW_API_KEY", "CLOUDFLARE_DNS_RECORD_ID", "SUPABASE_URL",
        "LINKEDIN_CLIENT_SECRET", "DB_HOST", "DB_PORT", "DB_USERNAME",
        "TWITTER_API_KEY", "TWITTER_API_SECRET", "LINKEDIN_CLIENT_ID",
        "GITHUB_TOKEN", "GITLAB_TOKEN", "BITBUCKET_KEY", "API_SECRET",
        "JIRA_CLIENT_ID", "TIKTOK_CLIENT_KEY", "TIKTOK_CLIENT_SECRET",
        "DUO_INTEGRATION_KEY", "DUO_SECRET_KEY", "SNOWFLAKE_ACCOUNT",
        "SNOWFLAKE_USERNAME", "SNOWFLAKE_PASSWORD", "HEROKU_API_KEY",
        "SQUARE_ACCESS_TOKEN", "TYPETALK_API_KEY", "CLICKUP_API_KEY",
        "KEYCLOAK_CLIENT_ID", "KEYCLOAK_CLIENT_SECRET", "VAULT_ADDR",
        "MIXPANEL_API_SECRET", "KARTRA_API_KEY", "KARTRA_API_SECRET",
        "ASANA_ACCESS_TOKEN", "BASECAMP_API_KEY", "BAMBOOHR_API_KEY",
        "JWT_EXPIRES_IN", "OTP_EXPIRE_TIME_SECONDS", "ACCESS_TOKEN",
        "ELASTICSEARCH_PASSWORD", "PLAID_CLIENT_ID", "PLAID_SECRET",
        "DATADOG_API_KEY", "ROLLBAR_ACCESS_TOKEN", "CIRCLECI_TOKEN",
        "GIPHY_API_KEY", "YOUTUBE_API_KEY", "YOUTUBE_CLIENT_SECRET",
        "TWILIO_FLEX_AUTH_TOKEN", "LINODE_API_KEY", "VULTR_API_KEY",
        "SHOPIFY_API_KEY", "SHOPIFY_API_SECRET", "ADOBE_CLIENT_ID",
        "GOOGLE_OAUTH_CLIENT_SECRET", "JWT_ISSUER", "JWT_AUDIENCE",
        "SENDGRID_API_KEY", "MAILGUN_API_KEY", "MAILCHIMP_API_KEY",
        "EKS_CLUSTER_NAME", "AKS_CLUSTER_NAME", "GKE_CLUSTER_NAME",
        "GOOGLE_API_KEY", "FACEBOOK_APP_ID", "FACEBOOK_APP_SECRET",
        "FIREBASE_PROJECT_ID", "MONGO_DB_URI", "MONGO_DB_USERNAME",
        "AZURE_STORAGE_ACCOUNT_NAME", "AZURE_STORAGE_ACCOUNT_KEY",
        "CYPRESS_API_KEY", "POSTMAN_API_KEY", "JENKINS_API_TOKEN",
        "FIREBASE_STORAGE_BUCKET", "FIREBASE_MESSAGING_SENDER_ID",
        "TOWER_API_KEY", "TOWER_API_SECRET", "BITLY_ACCESS_TOKEN",
        "MURAL_API_KEY", "YAMMER_ACCESS_TOKEN", "AZURE_CLIENT_ID",
        "REDIS_PORT", "ELASTICSEARCH_HOST", "ELASTICSEARCH_PORT",
        "OTP_TEXT", "TWILLIO_SENDER", "DB_URL", "PAYPAL_API_KEY",
        "ALGOLIA_APP_ID", "ALGOLIA_API_KEY", "AWS_SESSION_TOKEN",
        "HOTJAR_API_KEY", "SEGMENT_WRITE_KEY", "PINGDOM_API_KEY",
        "DROPBOX_ACCESS_TOKEN", "BOX_API_KEY", "BOX_API_SECRET",
        "WEBEX_ACCESS_TOKEN", "ZOOM_API_KEY", "ZOOM_API_SECRET",
        "DB_PASSWORD", "JWT_SECRET", "REFRESH_TOKEN", "USER_ID",
        "GCP_PROJECT_ID", "GCP_CLIENT_EMAIL", "GCP_PRIVATE_KEY",
        "PUSHER_SECRET", "PUSHER_CLUSTER", "SENTRY_AUTH_TOKEN",
        "TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "DEVICE_ID",
        "CLOUDBEES_API_KEY", "ZENHUB_API_KEY", "WAZUH_API_KEY",
        "AWS_S3_REGION", "AWS_S3_BUCKET", "AWS_ACCESS_KEY_ID",
        "SPLUNK_TOKEN", "HONEYBADGER_API_KEY", "HEAP_API_KEY",
        "DRIP_API_KEY", "GITHUB_APP_ID", "GITHUB_PRIVATE_KEY",
        "ZOHO_API_KEY", "SLACK_API_TOKEN", "TRELLO_API_KEY",
        "ONE_SIGNAL_API_KEY", "PUSHER_APP_ID", "PUSHER_KEY",
        "SUPABASE_KEY", "RENDER_API_KEY", "AUTH0_CLIENT_ID",
        "POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB",
        "KAFKA_BROKER", "KAFKA_API_KEY", "KAFKA_API_SECRET",
        "VAULT_TOKEN", "VAULT_ROLE_ID", "VAULT_SECRET_ID",
        "DOCKER_HUB_SECRET_KEY","SECRET_KEY"]
