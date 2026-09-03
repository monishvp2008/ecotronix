# Proprietary License
# Copyright (c) 2025 Monish. All rights reserved.
# Unauthorized copying, distribution, or modification is prohibited.

import os
import logging

from dotenv import load_dotenv

from livekit import agents
from livekit.agents import (
    Agent,
    AgentSession,
    RunContext,
    RoomInputOptions,
    function_tool,
)

from livekit.plugins import google, noise_cancellation

from weather import get_detailed_weather


# ---------------------------------------------------------
# ENVIRONMENT
# ---------------------------------------------------------

load_dotenv(".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------------------------------------------
# JARVIS AGENT
# ---------------------------------------------------------

class JarvisAgent(Agent):

    def __init__(
        self,
        language: str = "en",
        default_voice: str = "Puck"
    ) -> None:

        self.language = language

        # Gemini Live voices
        self.voice_map = {
            "en": "Puck",
            "ta": "Puck",
            "hi": "Puck",
            "te": "Puck",
        }

        self.voice = self.voice_map.get(
            language,
            default_voice
        )

        instructions = """
You are Jarvis, a smart and friendly voice AI assistant.

Your name is Jarvis.

Always introduce yourself as Jarvis when appropriate.

You can:
- Answer general questions
- Help users solve problems
- Give explanations
- Provide weather information using the weather tool
- Communicate naturally with the user

Keep your answers clear and reasonably concise.

The user's preferred language is English by default.

If the user asks you to speak in Tamil, Hindi, Telugu, or another language,
respond in that language.

When the user asks about weather, use the weather tool instead of guessing
weather information.
"""

        super().__init__(
            instructions=instructions
        )

    # -----------------------------------------------------
    # WEATHER TOOL
    # -----------------------------------------------------

    @function_tool()
    async def get_weather(
        self,
        context: RunContext,
        city: str
    ) -> str:
        """
        Get the current detailed weather information for a city.

        Args:
            city: The name of the city for which the user wants weather.
        """

        logging.info(
            f"Weather tool called for city: {city}"
        )

        api_key = os.getenv("6dd524e94d994178138353130da99e71")

        if not api_key:
            logging.error(
                "OPENWEATHER_API_KEY is missing."
            )

            return (
                "The weather API key is missing. "
                "Please check your .env file."
            )

        try:

            result = get_detailed_weather(
                city,
                api_key
            )

            logging.info(
                f"Weather result for {city}: {result}"
            )

            if not result:

                return (
                    "Sorry, I could not get the weather "
                    "information right now."
                )

            return result

        except Exception as e:

            logging.exception(
                f"Weather error for {city}: {e}"
            )

            return (
                "Sorry, I could not fetch the weather "
                "information right now."
            )


# ---------------------------------------------------------
# LIVEKIT ENTRYPOINT
# ---------------------------------------------------------

async def entrypoint(ctx: agents.JobContext):

    logging.info("Starting Jarvis agent...")

    jarvis_agent = JarvisAgent(
        language="en"
    )

    # -----------------------------------------------------
    # CHECK API KEYS
    # -----------------------------------------------------

    google_key = os.getenv("AIzaSyAWFk88T4h4Jbyg4Xy63E0O1B55FYeIlvg")
    weather_key = os.getenv("6dd524e94d994178138353130da99e71")

    logging.info(
        f"GOOGLE_API_KEY available: {bool(google_key)}"
    )

    logging.info(
        f"OPENWEATHER_API_KEY available: {bool(weather_key)}"
    )

    # -----------------------------------------------------
    # AGENT SESSION
    # -----------------------------------------------------

    session = AgentSession(

        llm=google.realtime.RealtimeModel(

            # Current Gemini Live model
            model="gemini-2.5-flash-native-audio-preview-12-2025",

            voice=jarvis_agent.voice,

            temperature=0.8,

            instructions=jarvis_agent.instructions,

        )
    )

    # -----------------------------------------------------
    # START SESSION
    # -----------------------------------------------------

    await session.start(

        room=ctx.room,

        agent=jarvis_agent,

        room_input_options=RoomInputOptions(

            noise_cancellation=noise_cancellation.BVC(),

        ),
    )

    logging.info(
        "Jarvis successfully joined the LiveKit room."
    )

    # -----------------------------------------------------
    # INITIAL GREETING
    # -----------------------------------------------------

    await session.generate_reply(

        instructions=(
            "Greet the user briefly. "
            "Introduce yourself as Jarvis "
            "and ask how you can help."
        )

    )

    logging.info(
        "Jarvis is running and ready for voice queries."
    )


# ---------------------------------------------------------
# START WORKER
# ---------------------------------------------------------

if __name__ == "__main__":

    agents.cli.run_app(
        agents.WorkerOptions(
            entrypoint_fnc=entrypoint
        )
    )