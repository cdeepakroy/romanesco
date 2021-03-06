import romanesco
import unittest


class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.add_three = {
            "inputs": [
                {
                    "name": "a",
                    "type": "number",
                    "format": "number"
                }
            ],
            "outputs": [
                {
                    "name": "b",
                    "type": "number",
                    "format": "number"
                }
            ],
            "mode": "python",
            "script": "b = a + 3"
        }

        self.add_two = {
            "inputs": [
                {
                    "name": "a",
                    "type": "number",
                    "format": "number"
                }
            ],
            "outputs": [
                {
                    "name": "b",
                    "type": "number",
                    "format": "number"
                }
            ],
            "mode": "python",
            "script": "b = a + 2"
        }

        self.add = {
            "inputs": [
                {
                    "name": "a",
                    "type": "number",
                    "format": "number",
                },
                {
                    "name": "b",
                    "type": "number",
                    "format": "number"
                }
            ],
            "outputs": [
                {
                    "name": "c",
                    "type": "number",
                    "format": "number"
                }
            ],
            "script": "c = a + b",
            "mode": "python"
        }

        self.multiply = {
            "inputs": [
                {
                    "name": "in1",
                    "type": "number",
                    "format": "number"
                },
                {
                    "name": "in2",
                    "type": "number",
                    "format": "number"
                }
            ],
            "outputs": [
                {
                    "name": "out",
                    "type": "number",
                    "format": "number"
                }
            ],
            "mode": "python",
            "script": "out = in1 * in2"
        }

        self.workflow = {
            "mode": "workflow",
            "inputs": [
                {
                    "name": "x",
                    "type": "number",
                    "format": "number",
                    "default": {"format": "number", "data": 10}
                },
                {
                    "name": "y",
                    "type": "number",
                    "format": "number"
                }
            ],
            "outputs": [
                {
                    "name": "result",
                    "type": "number",
                    "format": "number"
                }
            ],
            "steps": [
                {
                    "name": "af352b243109c4235d2549",
                    "task": self.add_three,
                },
                {
                    "name": "af352b243109c4235d25fb",
                    "task": self.add_two,
                },
                {
                    "name": "af352b243109c4235d25ec",
                    "task": self.multiply,
                }
            ],
            "connections": [
                {
                    "name": "x",
                    "input_step": "af352b243109c4235d2549",
                    "input": "a"
                },
                {
                    "name": "y",
                    "input_step": "af352b243109c4235d25fb",
                    "input": "a"
                },
                {
                    "output_step": "af352b243109c4235d2549",
                    "output": "b",
                    "input_step": "af352b243109c4235d25ec",
                    "input": "in1"
                },
                {
                    "output_step": "af352b243109c4235d25fb",
                    "output": "b",
                    "input_step": "af352b243109c4235d25ec",
                    "input": "in2"
                },
                {
                    "name": "result",
                    "output_step": "af352b243109c4235d25ec",
                    "output": "out"
                }
            ]
        }

        self.multi_input = {
            "mode": "workflow",
            "inputs": [
                {
                    "name": "x",
                    "type": "number",
                    "format": "number"
                },
                {
                    "name": "y",
                    "type": "number",
                    "format": "number"
                }
            ],
            "outputs": [
                {
                    "name": "result",
                    "type": "number",
                    "format": "number"
                }
            ],
            "steps": [
                {
                    "name": 1,
                    "task": self.add,
                },
                {
                    "name": 2,
                    "task": self.multiply,
                },
                {
                    "name": 3,
                    "task": self.multiply,
                }
            ],
            "connections": [
                {
                    "name": "x",
                    "input_step": 2,
                    "input": "in1"
                },
                {
                    "name": "x",
                    "input_step": 2,
                    "input": "in2"
                },
                {
                    "name": "y",
                    "input_step": 3,
                    "input": "in1"
                },
                {
                    "name": "y",
                    "input_step": 3,
                    "input": "in2"
                },
                {
                    "output_step": 2,
                    "output": "out",
                    "input_step": 1,
                    "input": "a"
                },
                {
                    "output_step": 3,
                    "output": "out",
                    "input_step": 1,
                    "input": "b"
                },
                {
                    "name": "result",
                    "output_step": 1,
                    "output": "c"
                }
            ]
        }

        self.visualization = {
            "mode": "workflow",
            "inputs": [
                {
                    "name": "x",
                    "type": "number",
                    "format": "number"
                },
                {
                    "name": "y",
                    "type": "number",
                    "format": "number"
                }
            ],
            "outputs": [
                {
                    "name": "result",
                    "type": "number",
                    "format": "number"
                }
            ],
            "steps": [
                {
                    "name": 1,
                    "task": self.add,
                },
                {
                    "name": 2,
                    "task": self.multiply,
                },
                {
                    "name": 3,
                    "task": self.multiply,
                },
                {
                    "name": 4,
                    "visualization": True,
                    "task": {
                        "inputs": [
                            {
                                "name": "x",
                                "type": "number",
                                "format": "number"
                            }
                        ]
                    }
                }
            ],
            "connections": [
                {
                    "name": "x",
                    "input_step": 2,
                    "input": "in1"
                },
                {
                    "name": "x",
                    "input_step": 2,
                    "input": "in2"
                },
                {
                    "name": "y",
                    "input_step": 3,
                    "input": "in1"
                },
                {
                    "name": "y",
                    "input_step": 3,
                    "input": "in2"
                },
                {
                    "output_step": 2,
                    "output": "out",
                    "input_step": 1,
                    "input": "a"
                },
                {
                    "output_step": 3,
                    "output": "out",
                    "input_step": 1,
                    "input": "b"
                },
                {
                    "name": "result",
                    "output_step": 1,
                    "output": "c"
                },
                {
                    "output_step": 1,
                    "output": "c",
                    "input_step": 4,
                    "input": "x"
                }
            ]
        }

    def test_workflow(self):
        outputs = romanesco.run(
            self.workflow,
            inputs={
                "x": {"format": "json", "data": "1"},
                "y": {"format": "number", "data": 2}
            })
        self.assertEqual(outputs["result"]["format"], "number")
        self.assertEqual(outputs["result"]["data"], (1+3)*(2+2))

        # Test using the default value for x (10).
        outputs = romanesco.run(
            self.workflow,
            inputs={
                "y": {"format": "number", "data": 2}
            })
        self.assertEqual(outputs["result"]["format"], "number")
        self.assertEqual(outputs["result"]["data"], (10+3)*(2+2))

    def test_multi_input(self):
        outputs = romanesco.run(
            self.multi_input,
            inputs={
                "x": {"format": "number", "data": 2},
                "y": {"format": "number", "data": 3}
            })
        self.assertEqual(outputs["result"]["format"], "number")
        self.assertEqual(outputs["result"]["data"], (2*2)+(3*3))

    def test_visualization(self):
        outputs = romanesco.run(
            self.visualization,
            inputs={
                "x": {"format": "number", "data": 2},
                "y": {"format": "number", "data": 3}
            })
        self.assertEqual(outputs["result"]["format"], "number")
        self.assertEqual(outputs["result"]["data"], (2*2)+(3*3))
        self.assertEqual(outputs["_visualizations"], [{
            "mode": "preset",
            "type": 4,
            "inputs": {
                "x": {
                    "format": "number",
                    "data": (2*2)+(3*3)
                }
            }
        }])

if __name__ == '__main__':
    unittest.main()
