import apple_gpu


def test_accelerator_performance_statistics():
    statistics = apple_gpu.accelerator_performance_statistics()
    assert isinstance(statistics, dict)
