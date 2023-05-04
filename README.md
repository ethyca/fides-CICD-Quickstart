# Fides CI/CD Turnkey Quickstart

![Fides banner](https://github.com/ethyca/fides/blob/main/docs/fides/docs/img/fides-banner.png "Fides banner")

## :zap: Overview

Fides (pronounced */fee-dhez/*, from Latin: Fidēs) is an open-source privacy engineering platform for managing the fulfillment of data privacy requests in your runtime environment, and the enforcement of privacy regulations in your code.

## :rocket: Turnkey Quick Start

### Getting Started 

This repository provides a comprehensive example of a fictional ecommerce site for a CookieHouse, showcasing how Fides can be integrated into CI/CD pipelines to ensure privacy and regulatory compliance. The example consists of a turn-key solution, demonstrating the full process from building a database in CI to performing migrations against it. The CookieHouse example serves as a practical guide to understand how Fides can be applied in real-world scenarios.

In addition to this turn-key example, another repository will be available as a lab to help users set up their own CI/CD pipelines using Fides. By following the lab, you can learn how to establish a CI/CD pipeline tailored to your specific requirements while ensuring that privacy regulations are enforced in your code.

The Fides platform is designed to help organizations manage and fulfill Data Mapping, Consent, and Data Privacy Requests while staying compliant with various privacy regulations. By using Fides in your CI/CD pipeline, you can ensure that your company remains compliant, reducing the risk of privacy breaches and potential fines.

#### Minimum requirements

* [Docker](https://www.docker.com/products/docker-desktop) (version 20.10.11 or later)
* [Python](https://www.python.org/downloads/) (version 3.8 through 3.10)

## :books: How this works

### Repository Structure

#### .fides - The `.fides` folder is required for each repository for privacy checks.

 This folder acts as a place where all Fides and repo specific configurations live. This can include:
  1. The Database Privacy Declarations known as a [Dataset](https://docs.ethyca.com/fides/dsr_quickstart/dsr_support/datasets)  (`cookiehouse_core.yml`). This can be autocompleted using Fide's AI Classification tools or an empty skeleton can be generated using [Fides Generate](https://docs.ethyca.com/fides/cli_support/generate_resources#command-line)
  2. The initial fides configurations (`fides.toml`)
  3. A codified version of your privacy policy (`policy.yml`)
  
The privacy declarations and privacy policy use [FidesLang Taxonomy](https://ethyca.github.io/fideslang/explorer/), the universal privacy language of the web!

#### .github/workflows - This contains the CI job that will perform the migration and perform the privacy checks

The example CI job performs the following steps:
  1. **Checkout:** Retrieves the source code for the repository using the actions/checkout action. 
  2. **Set up Python:** Sets up the Python environment using the actions/setup-python action, specifying Python version 3.10.
  3. **Install Fides:**  Installs the `ethyca-fides` library with version 2.12.0 using the `pip install` command.
  4. **Run Database Migrations:** Executes a Python script (`db_migration.py`) responsible for running database migrations against our fictional database for CookieHouse.
  5. **Scan Database and Validate that all fields are Accounted for:** This is the first step to validate that you are in compliance. The `fides --local scan dataset db` command checks to see if any net-new fields were introduced into the database but weren't annotated in `cookiehouse_core.yml`. This outputs a report that shows what is missing and what your percent privacy coverage is. An example report is below:

```

```

## :bulb: Additional Information

### Documentation

For more information on getting started with Fides, how to configure and set up Fides, and more about the Fides ecosystem of open source projects:

* Documentation: <https://docs.ethyca.com>
* Taxonomy: <https://ethyca.github.io/fideslang/explorer/>
* Website: www.ethyca.com/fides

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
Fides tools are built on [fideslang](https://github.com/ethyca/privacy-taxonomy), the Fides language specification, which is licensed under [CC by 4](https://github.com/ethyca/privacy-taxonomy/blob/main/LICENSE).

Fides is created and sponsored by Ethyca: a developer tools company building the trust infrastructure of the internet. If you have questions or need assistance getting started, let us know at fides@ethyca.com!

[release-image]: https://img.shields.io/github/release/ethyca/fides.svg
[release-url]: https://github.com/ethyca/fides/releases
[docker-workflow-image]: https://github.com/ethyca/fides/workflows/Docker%20Build%20&%20Push/badge.svg
[docs-workflow-image]: https://github.com/ethyca/fides/workflows/Publish%20Docs/badge.svg
[release-workflow-image]: https://github.com/ethyca/fides/actions/workflows/publish_package.yaml/badge.svg
[docker-actions-url]: https://github.com/ethyca/fides/actions/workflows/publish_docker.yaml
[docs-actions-url]: https://github.com/ethyca/fides/actions/workflows/publish_docs.yaml
[publish-actions-url]: https://github.com/ethyca/fides/actions/workflows/publish_package.yaml
[license-image]: https://img.shields.io/:license-Apache%202-blue.svg
[license-url]: https://www.apache.org/licenses/LICENSE-2.0.txt
[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black/
[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: http://mypy-lang.org/
[twitter-image]: https://img.shields.io/twitter/follow/ethyca?style=social
[twitter-url]: https://twitter.com/ethyca
