from typing import Optional
from google.auth import credentials
import vertexai
from google.cloud import aiplatform
from google.cloud import aiplatform_v1
from vertexai.generative_models import GenerativeModel, Part


def init_sample(
    project: Optional[str] = None,
    location: Optional[str] = None,
    experiment: Optional[str] = None,
    staging_bucket: Optional[str] = None,
    credentials: Optional[credentials.Credentials] = None,
    encryption_spec_key_name: Optional[str] = None,
    service_account: Optional[str] = None,
):

    from google.cloud import aiplatform

    aiplatform.init(
        project=project,
        location=location,
        experiment=experiment,
        staging_bucket=staging_bucket,
        credentials=credentials,
        encryption_spec_key_name=encryption_spec_key_name,
        service_account=service_account,
    )



# TODO(developer): Update and un-comment below lines
project_id = "hallowed-trail-424618-e5"

vertexai.init(project=project_id, location="europe-west4")

model = GenerativeModel(model_name="gemini-1.5-flash-001")

prompt = """
You are a very competent pdf to text conversion program.
Convert the following pdfs to easily readable text that can be interpreted by a LLM.
"""

pdf_file_uri = "gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf"
pdf_file = Part.from_uri(pdf_file_uri, mime_type="application/pdf")
contents = [pdf_file, prompt]

response = model.generate_content(contents)
print(response.text)