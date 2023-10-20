from __future__ import annotations
import objc
import Foundation

IOKit = Foundation.NSBundle.bundleWithIdentifier_("com.apple.framework.IOKit")

functions = [
    ("IOServiceGetMatchingService", b"II@"),
    ("IOServiceMatching", b"@*"),
    ("IORegistryEntryCreateCFProperties", b"IIo^@@I"),
]

objc.loadBundleFunctions(IOKit, globals(), functions)


def accelerator_performance_statistics() -> dict[str, int]:
    accelerator_info = IOServiceGetMatchingService(
        0, IOServiceMatching(b"IOAccelerator")
    )
    if accelerator_info == 0:
        raise RuntimeError("IOAccelerator not found")
    # else...
    err, props = IORegistryEntryCreateCFProperties(accelerator_info, None, None, 0)
    if err != 0:
        raise RuntimeError("IOAccelerator properties not found")
    # else...
    return dict(props["PerformanceStatistics"])
