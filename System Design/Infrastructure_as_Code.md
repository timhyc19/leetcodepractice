```
The purpose of IAC with terraform is to organize all cloud services in a code like structure.
Rather than trying to create, delete, update, edit resources on the console, maintaining all of the information
in a codebase makes it more accessible, faster to change / deploy, and secure.

Form the structure above, our modules consisted of folders for certain tasks that required GCP services
Some examples include cloud-composers, feature store, networking, etc....
Each of these folders typically had .tf files such as service accounts.tf, variables.tf, which basically
defined resources, and their information.  


One of my first uses of terraform was creating the barebones resources for the upgration of GCP services
- Composer V2 
    --> used to deploy airflow services; holds dags, and gives access to airflow UI 
    --> Environment Configurations, Software Configurations, Node Configurations
    --> Code looked like something below (composer_v2.tf):
    
resource "google_composer_environment" "cloud-composer-environment-v2" {
  name   = "${var.env}-v2"
  region = var.region
  config {

    node_config {
      service_account = google_service_account.composer-worker.name
      network         = var.node_network_name
      subnetwork      = var.node_subnetwork_name
      ip_allocation_policy {
        cluster_secondary_range_name  = var.cluster_secondary_ip_range_name
        services_secondary_range_name = var.services_secondary_ip_range_name
      }
    }

    software_config {
      image_version = "composer-2.2.1-airflow-2.5.1"

      airflow_config_overrides = {
        core-dags_are_paused_at_creation = "True"
        # Increase the time before a task is declared a zombie and terminated
        # This was happening frequently for longer KubernetesPodOperator tasks
        scheduler-scheduler_zombie_task_threshold = 1800 # time in seconds
        api-auth_backends                         = "airflow.api.auth.backend.basic_auth"
      }

      env_variables = {
        ENV = var.env
      }
    }
  }
  depends_on = [
    google_project_iam_member.composer-worker,
    google_service_account_iam_binding.composer_sa_service_account_user,
    google_service_account_iam_member.composer_sa_service_agent_v2_ext,
    google_project_iam_member.composer_agent_v2_ext,
  ]
}

Other terraform resources I created was the invisible guard pub/sub resources for the state-manager in home-guard
Then, in each of the dev, stage, prod project folders, there are .tf files declaring the variable values for each project
--> some projects used different service accounts, typically dev environment was just testing stuff and experimenting, while
stage and prod were more securely measured and properly formatted (restrictired access to service accounts, etc...)

What is a service account in gcp?
--> any resource or any action performed requires specific permissions for the action to go through
Service accounts act as "users" that hold IAM (Identity and Access Management) roles, and they can only perform those roles
Each service account holds a public-private key pair. The private key is securely stored by the client (application or service), while the public key is uploaded to GCP.
So in relation to terraform, being able to limit service account access to certain resources allows for more security
```