import logging
from shape_manager import ShapeManager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    logger.info("The program started running.")  # רישום הודעת מידע
    manager = ShapeManager()

    # ... כאן יבוא שאר הקוד של התפריט שלך ...


if __name__ == "__main__":
    main()