# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# Copyright © 2024 Manifold Labs

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


import pydantic

from typing import List



class ChallengeSamplingParams(pydantic.BaseModel):
    '''
    SamplingParams is a pydantic model that represents the sampling parameters for the TGI model.
    '''
    best_of: int = pydantic.Field(
        1,
        title="Best of",
        description="The number of samples to generate.",
    )

    decoder_input_details: bool = pydantic.Field(
        True,
        title="Decoder Input Details",
        description="Whether to return the decoder input details.",
    )

    details: bool = pydantic.Field(
        False,
        title="Details",
        description="Whether to return the details.",
    )

    do_sample: bool = pydantic.Field(
        True,
        title="Do Sample",
        description="Whether to sample.",
    )

    max_new_tokens: int = pydantic.Field(
        16,
        title="Max New Tokens",
        description="The maximum number of tokens to generate in the completion.",
    )

    repetition_penalty: float = pydantic.Field(
        1.0,
        title="Repetition Penalty",
        description="The repetition penalty.",
    )

    return_full_text: bool = pydantic.Field(
        False,
        title="Return Full Text",
        description="Whether to return the full text.",
    )

    seed: int = pydantic.Field(
        None,
        title="Seed",
        description="The seed used to generate the output.",
    )

    stop: List[str] = pydantic.Field(
        [""],
        title="Stop",
        description="The stop words.",
    )

    temperature: float = pydantic.Field(
        1e-3,
        title="Temperature",
        description="Sampling temperature to use, between 0 and 2.",
    )

    top_k: int = pydantic.Field(
        10,
        title="Top K",
        description="Nucleus sampling parameter, top_p probability mass.",
    )

    top_n_tokens: int = pydantic.Field(
        5,
        title="Top N Tokens",
        description="The number of tokens to return.",
    )

    top_p: float = pydantic.Field(
        0.9999999,
        title="Top P",
        description="Nucleus sampling parameter, top_p probability mass.",
    )

    truncate: int = pydantic.Field(
        None,
        title="Truncate",
        description="The truncation length.",
    )

    typical_p: float = pydantic.Field(
        0.9999999,
        title="Typical P",
        description="The typical probability.",
    )

    watermark: bool = pydantic.Field(
        False,
        title="Watermark",
        description="Whether to watermark.",
    )

class ChallengeRequest(pydantic.BaseModel):
    '''
    ChallengeRequest is a pydantic model that represents the request to the TGI model.
    '''
    private_input: dict = pydantic.Field(
        ...,
        title="Private Input",
        description="The private input.",
    )
    sampling_params: ChallengeSamplingParams = pydantic.Field(
        ...,
        title="Sampling Params",
        description="The sampling parameters.",
    )
    