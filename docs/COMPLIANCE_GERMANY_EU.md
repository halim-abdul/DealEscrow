# Germany / EU Compliance Baseline

> Engineering research notes only; not legal advice.

## 1. Payment-services perimeter

Whether DealEscrow would need regulatory authorisation depends on the actual business model and how payments are handled. BaFin states that a provider taking possession of customer funds will likely need payment-services or e-money authorisation, while a provider that merely supplies technical infrastructure and leaves payment execution to a cooperating payment-service provider may potentially fall within a technical-service-provider exception.

**Engineering consequence:** DealEscrow should integrate with an appropriately authorised payment provider rather than hold customer funds itself unless the operating entity has the required authorisation.

Source: BaFin, “Benötige ich für meine Tätigkeit eine Erlaubnis der BaFin?”  
https://www.bafin.de/ref/19629832

## 2. Credit-intermediation perimeter

BaFin has explained that pure intermediation between lenders and borrowers is not automatically banking business, but whether the platform or its users trigger an authorisation requirement must be assessed case by case based on how the activity is actually conducted.

**Engineering consequence:** do not represent every user as being free to “operate like a small bank.” Add a regulatory-classification gate before enabling repeated/professional lending activity.

Source: BaFin Quarterly, discussion of credit intermediation platforms.

## 3. Direct debit

The Deutsche Bundesbank explains that a SEPA direct debit is legally based on a mandate that contains both the payer's consent to collection and the instruction to the payer's payment service provider.

**Engineering consequence:** no automatic debit without a valid active mandate and a compliant provider integration. The platform must retain evidence of mandate status and revocation.

Source: Deutsche Bundesbank, SEPA Direct Debit  
https://www.bundesbank.de/en/tasks/payment-systems/services/sepa/content/sepa-direct-debit-626654

## 4. Default interest

German BGB § 288 contains statutory rules for interest during debtor default, including different treatment for certain transactions where no consumer is involved.

**Engineering consequence:** never hard-code “5% after 45 days” as German law. Distinguish:
- contractual interest,
- grace period,
- default interest,
- consumer/non-consumer context,
- current base-rate-dependent rules.

Source: BGB § 288  
https://www.gesetze-im-internet.de/bgb/__288.html

## 5. GDPR data minimisation

GDPR Article 5 requires personal data to be adequate, relevant and limited to what is necessary for the processing purpose.

**Engineering consequence:** do not create a giant biography database merely because the fields might be useful. Identity, DOB, birthplace and citizenship need a defined purpose and lawful basis, with retention/deletion controls.

Source: Regulation (EU) 2016/679, Article 5  
https://eur-lex.europa.eu/eli/reg/2016/679/oj

## 6. Criminal-record / PCC information

GDPR Article 10 places special restrictions on processing personal data relating to criminal convictions and offences.

**Engineering consequence:** PCC/criminal-history data is not a default risk feature. Do not upload or score it unless a concrete lawful basis, appropriate safeguards and jurisdiction-specific review have been established.

## 7. Human review

The following events require a human compliance/legal checkpoint:
- legal notice generation,
- collections escalation,
- disputed liability,
- regulatory classification,
- identity/criminal-record matters,
- consequential risk decisions.

AI can retrieve and summarise relevant materials, but it must not independently declare legal liability or issue binding legal conclusions.
