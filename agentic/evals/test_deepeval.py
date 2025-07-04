import pytest
from deepeval import assert_test
from deepeval.metrics.answer_relevancy.answer_relevancy import AnswerRelevancyMetric
from deepeval.metrics.hallucination.hallucination import HallucinationMetric
from deepeval.metrics.g_eval.g_eval import GEval
from deepeval.test_case.llm_test_case import LLMTestCase, LLMTestCaseParams


from dotenv import load_dotenv
load_dotenv()

def test_geval():
    metric = GEval(
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5
    )  
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output="You have 30 days to get a full refund at no extra cost.",
        expected_output="We offer a 30-day full refund at no extra costs.",
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra costs."]
    )

  
    assert_test(test_case, [metric])


def test_retrieval_context():
    metric = AnswerRelevancyMetric(threshold=0.7)
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        # Replace this with the actual output from your LLM application
        actual_output="We offer a 30-day full refund at no extra costs.",
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra costs."]
    )

    assert_test(test_case, [metric])

def test_hallucination():
    metric = HallucinationMetric(threshold=0.7)
    test_case = LLMTestCase(
        input="How many evaluation metrics does DeepEval offers?",
        actual_output="14+ evaluation metrics",
        context=["DeepEval offers 14+ evaluation metrics"]
    )
    
    assert_test(test_case, [metric])    