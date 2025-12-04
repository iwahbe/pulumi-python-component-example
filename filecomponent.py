"""A Python component that wraps the file provider example."""

import pulumi
from typing import TypedDict

# Import the generated SDK
from example_file import File


class FileComponentArgs(TypedDict):
    """Arguments for the FileComponent."""
    content: pulumi.Input[str]
    path: pulumi.Input[str]
    force: pulumi.Input[bool]


class FileComponent(pulumi.ComponentResource):
    """A component resource that creates a file with enhanced functionality."""

    file: pulumi.Output[str]

    def __init__(
        self,
        name: str,
        args: FileComponentArgs,
        opts: pulumi.ResourceOptions = None
    ):
        """
        Create a FileComponent resource.

        Args:
            name: The name of the resource.
            args: The arguments for the component.
            opts: Resource options.
        """
        super().__init__("file-component:index:FileComponent", name, {}, opts)

        # Create the underlying File resource
        file = File(
            f"{name}-file",
            content=args["content"],
            path=args["path"],
            force=args.get("force", False),
            opts=pulumi.ResourceOptions(parent=self)
        )

        # Export outputs
        self.file = file.path

        # Register outputs
        self.register_outputs({
            "file": self.file
        })
