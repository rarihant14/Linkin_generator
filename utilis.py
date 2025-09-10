def check_media_relevance(llm, post_text: str, file_name: str) -> str:
    """
    Use Gemini to check if the uploaded image/video is relevant to the post.
    Returns "Relevant" or "Not Relevant".
    """
    relevance_prompt = f"""
    The user wrote this LinkedIn post:

    {post_text}

    They uploaded a media file named: "{file_name}".

    Based on the file name and type, decide if this media could be relevant
    to the post content. Respond with only "Relevant" or "Not Relevant".
    """
    response = llm.invoke(relevance_prompt)
    return response.content.strip()
