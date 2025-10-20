# Privacy Impact Assessment - Sentiment Classifier

## Data Collection

- **What data is collected?**:
  - Text input for sentiment analysis
  - Prediction results and confidence scores
  - Usage timestamps
  - No personally identifiable information (PII)

- **How is data collected?**:
  - API requests from client applications
  - Batch processing uploads
  - All collection is explicit and user-initiated

- **Purpose of collection**:
  - Providing sentiment analysis service
  - Model performance monitoring
  - Service improvement and debugging

## Data Usage

- **How is data used?**:
  - Real-time prediction generation
  - Aggregate statistics for monitoring
  - Model retraining (anonymized samples only)

- **Who has access?**:
  - ML engineers: Read-only access to anonymized data
  - Data scientists: Access to aggregate metrics only
  - System administrators: Infrastructure access only
  - No third-party access

- **Retention period**:
  - Raw predictions: 30 days
  - Aggregate metrics: 1 year
  - Training data samples: Until model retirement
  - All data deleted upon user request

## Data Protection

- **Security measures**:
  - Encryption at rest (AES-256)
  - Encryption in transit (TLS 1.3)
  - Access logging and monitoring
  - Regular security audits

- **Encryption**:
  - All data encrypted at rest in database
  - HTTPS required for all API endpoints
  - No data transmitted over unencrypted channels

- **Access controls**:
  - Role-based access control (RBAC)
  - Multi-factor authentication required
  - Principle of least privilege
  - Regular access reviews

## User Rights

- **Right to access**:
  - Users can request all data associated with their account
  - Response within 30 days
  - Data provided in machine-readable format (JSON)

- **Right to deletion**:
  - Users can request deletion of all their data
  - Deletion completed within 30 days
  - Confirmation provided upon completion

- **Right to rectification**:
  - Users can request correction of inaccurate data
  - Changes processed within 14 days
  - Notification of changes provided

## Compliance

- **Regulations**:
  - GDPR compliant (EU)
  - CCPA compliant (California)
  - Data Protection Act 2018 (UK)

- **Data Protection Officer**:
  - Contact: dpo@example.com
  - Available for privacy inquiries

- **Last Review**: 2025-10-20

- **Next Scheduled Review**: 2026-10-20

## Risk Assessment

- **Identified Risks**:
  - Low risk of data breach (strong encryption)
  - Low risk of re-identification (no PII collected)
  - Medium risk of model memorization (mitigated by differential privacy)

- **Mitigation Measures**:
  - Regular security testing
  - Automated PII detection in inputs
  - Rate limiting to prevent data extraction
  - Monitoring for unusual access patterns

## Changes Log

- **2025-10-20**: Initial assessment
