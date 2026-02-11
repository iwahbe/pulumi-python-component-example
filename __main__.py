"""Entry point for the random component provider."""

from pulumi.provider.experimental import component_provider_host
from randomcomponent import RandomComponent


if __name__ == "__main__":
    component_provider_host(
        name="random-component",
        components=[RandomComponent]
    )
