"""Entry point for the file component provider."""

from pulumi.provider.experimental import component_provider_host
from filecomponent import FileComponent


if __name__ == "__main__":
    component_provider_host(
        name="file-component",
        components=[FileComponent]
    )
