from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from schemas.models import Task
from config import logger
from task_manager.tasks import MemoryTaskManager
from data.dataframes import DataProcessor, PandasHandler, PolarsHandler


# ------------------------------------------------------------------------------
# API ROUTERS
# ------------------------------------------------------------------------------
router = APIRouter()

# ------------------------------------------------------------------------------
# TASK MANAGER INSTANCES
# ------------------------------------------------------------------------------
task_manager = MemoryTaskManager(
    logs=logger
)

# ------------------------------------------------------------------------------
# DATAFRAME MANAGER INSTANCES
# ------------------------------------------------------------------------------
dataframe_processor = DataProcessor(
    dataframe_processor=PolarsHandler()
)

@router.post("/v2/tasks")
async def create_task(
        request: Task
):
    logger.info(f"Creating task: {request.title}")
    task_manager.save(request)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "Title": request.title,
            "Description": request.description,
            "Priority": request.priority
        }
    )


@router.get("/v2/dataframes")
async def dataframes():
    return dataframe_processor.show_data()
