# Fides CI/CD Turnkey Quickstart

![Fides banner](https://github.com/ethyca/fides/blob/main/docs/fides/docs/img/fides-banner.png "Fides banner")

## :zap: Overview

Fides (pronounced */fee-dhez/*, from Latin: Fidēs) is an open-source privacy engineering platform for managing the fulfillment of data privacy requests in your runtime environment, and the enforcement of privacy regulations in your code.

## :rocket: Turnkey Quickstart

### Getting Started

This repository provides a comprehensive example of a fictional ecommerce site for a CookieHouse, showcasing how Fides can be integrated into CI/CD pipelines to ensure privacy and regulatory compliance. The example consists of a turn-key solution, demonstrating the full process from building a database in CI to performing migrations against it. The CookieHouse example serves as a practical guide to understand how Fides can be applied in real-world scenarios.

The Fides platform is designed to help organizations manage and fulfill Data Mapping, Consent, and Data Privacy Requests while staying compliant with various privacy regulations. By using Fides in your CI/CD pipeline, you can ensure that your company remains compliant, reducing the risk of privacy breaches and potential fines.

#### Minimum requirements

* [Docker](https://www.docker.com/products/docker-desktop) (version 20.10.11 or later, must include Docker Compose)
* [Python](https://www.python.org/downloads/) (version 3.8 through 3.10)

## :books: How this works

### Repository Structure

```txt
.
├── .fides
│   ├── cookiehouse_core.yml
│   ├── fides.toml
│   └── policy.yml
├── .github
│   └── workflows
│       └── fides_ci.yml
├── README.md
├── database
│   └── migrations
│       └── postgres_sample.sql
├── db_migration.py
└── docker-compose.yml

```

### .fides

------

The `.fides` directory is generally required for privacy checks within each repo. While another directory may be specific, `.fides` is the default expected path for Fides-related resources.

This folder acts as a place where all Fides and repo specific configurations live. This can include:

  1. The Database Privacy Declarations known as a [Dataset](https://docs.ethyca.com/fides/dsr_quickstart/dsr_support/datasets)  (`cookiehouse_core.yml`). This can be autocompleted using Fides's AI Classification tools or an empty skeleton can be generated using [Fides Generate](https://docs.ethyca.com/fides/cli_support/generate_resources#command-line)

  2. The initial Fides configurations (`fides.toml`)

  3. A codified version of your privacy policy (`policy.yml`)
  
The privacy declarations and privacy policy use [FidesLang Taxonomy](https://ethyca.github.io/fideslang/explorer/), the universal privacy language of the web!

### .github/workflows

------

This folder contains the CI job that will perform the sample database migration and perform the privacy checks.

The example CI job performs the following steps:

  1. **Checkout:** Retrieves the source code for the repository using the actions/checkout action.

  2. **Set up Python:** Sets up the Python environment using the actions/setup-python action, specifying Python version 3.10.

  3. **Install Fides:**  Installs the `ethyca-fides` library with version 2.20.1 using the `pip install` command.

  4. **Run Database Migrations:** Executes a Python script (`db_migration.py`) responsible for running database migrations against our fictional database for CookieHouse.

  5. **Scan Database and Validate that all fields are Accounted for:** This is the first step to validate that you are in compliance. The `fides --local scan dataset db` command checks to see if any net-new fields were introduced into the database but weren't annotated in `cookiehouse_core.yml`. This outputs a report that shows what is missing and what your percent privacy coverage is. You can potentially use this for branch protections or keep this as a warning. An example report is below:

```sh
Loading resource manifests from: .fides/
Taxonomy successfully created.
Loaded the following dataset manifests:
	cookiehouse_core
Successfully scanned the following datasets:
	public

The following fields are missing data category annotations:
 public.users.name
 public.users.phone
 public.orders.billingAddress

Annotation coverage: 82%
```

  6. **Evaluation:** Performs a Privacy Policy Evaluation using Fides. This step runs the command `fides --local evaluate` and the evaluation process uses the `policy.yml` to validate that data annotated in `cookiehouse_core.yml` are compliant. An Example output with a violation on `user.demographic.date_of_birth` is shown below:

```sh
Loaded config from: .fides/fides.toml
Loading resource manifests from: .fides/
Taxonomy successfully created.
----------
Processing organization resource(s)...
WOULD CREATE 0 organization resource(s).
WOULD UPDATE 1 organization resource(s).
----------
Processing system resource(s)...
WOULD CREATE 0 system resource(s).
WOULD UPDATE 4 system resource(s).
----------
Processing policy resource(s)...
WOULD CREATE 0 policy resource(s).
WOULD UPDATE 1 policy resource(s).
----------
Processing dataset resource(s)...
WOULD CREATE 0 dataset resource(s).
WOULD UPDATE 5 dataset resource(s).
----------
Loading resource manifests from: .fides/
Taxonomy successfully created.
Evaluating the following policies:
- webapp_data_policy
----------
Checking for missing resources...
Executing Policy evaluation(s)...
{ 'fides_key': '54bfd260_1665_42aa_97a4_89fd3af395d8',
  'message': None,
  'status': <StatusEnum.FAIL: 'FAIL'>,
  'violations': [ { 'detail': 'Declaration (Storing customer data) of system '
                              '(CookieHouse_Core) failed rule (Reject '
                              'Sensitive Data) from policy '
                              '(webapp_data_policy) for dataset field (DOB). '
                              'Violated usage of data categories '
                              '(user.demographic.date_of_birth) with qualifier '
                              '(aggregated.anonymized.unlinked_pseudonymized.pseudonymized.identified) '
                              'for data uses (functional) and subjects '
                              '(customer)',
                    'violating_attributes': { 'data_categories': [ 'user.demographic.date_of_birth'],
                                              'data_qualifier': 'aggregated.anonymized.unlinked_pseudonymized.pseudonymized.identified',
                                              'data_subjects': ['customer'],
                                              'data_uses': [ 'functional']}}]}
```
  
**A few things to note:**

  1. You can customize this flow to match your organization's needs.
  2. Consider using some of these checks as branch protections to prevent PRs from being merged in that are not compliant with your privacy policy(ies).

## :bulb: Additional Information

### Documentation

For more information on getting started with Fides, how to configure and set up Fides, and more about the Fides ecosystem of open source projects:

* Documentation: <https://docs.ethyca.com>
* Taxonomy: <https://ethyca.github.io/fideslang/explorer/>
* Website: <https://docs.ethyca.com/fides/overview>

### Support

Join the conversation on:

* [Slack](https://fid.es/join-slack)
* [Twitter](https://twitter.com/ethyca)
* [Discussions](https://github.com/ethyca/fides/discussions)

### Contributing

We welcome and encourage all types of contributions and improvements!  Please see our [contribution guide](https://docs.ethyca.com/fides/community/overview) to opening issues for bugs, new features, and security or experience enhancements.

Read about the [Fides community](https://docs.ethyca.com/fides/community/hints_tips) or dive into the [contributor guides](https://docs.ethyca.com/fides/community/development/overview) for information about contributions, documentation, code style, testing and more. Ethyca is committed to fostering a safe and collaborative environment, such that all interactions are governed by the [Fides Code of Conduct](https://docs.ethyca.com/fides/community/code_of_conduct).

## :balance_scale: License

The [Fides](https://github.com/ethyca/fides) ecosystem of tools are licensed under the [Apache Software License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
Fides tools are built on [Fideslang](https://github.com/ethyca/privacy-taxonomy), the Fides language specification, which is licensed under [CC by 4](https://github.com/ethyca/privacy-taxonomy/blob/main/LICENSE).

Fides is created and sponsored by Ethyca: a developer tools company building the trust infrastructure of the internet. If you have questions or need assistance getting started, let us know at fides@ethyca.com!
