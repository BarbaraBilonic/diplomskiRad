from models import *

def createProject(projectData):
    try:
        projectRecord=Project.objects.create(name=projectData['name'])
        projectRecord.save()
        if projectRecord.id:
            return 200
        else:
            return 400

    except:
        return 400


def createTestPlan(testPlanData):
    try:
        testPlanRecord=TestPlan(name=testPlanData['name'],startDate=testPlanData['startDate'],endDate=testPlanData['endDate'],project=testPlanData['projectID'])
        testPlanRecord.save()
        if testPlanRecord.id:
            return 200
        else:
            return 400
    except:
        return 400

def createTestObjective(testObjectiveData):
    try:
        testObjectiveRecord=TestObjective(name=testObjectiveData['name'],testPlanId=testObjectiveData['testPlanID'])
        if testObjectiveRecord.id:
            return 200
        else:
            return 400
    except:
        return 400

def createTest(testData):
    try: 
        testRecord=Test(
            name=testData['name'],
            testObjectiveId=testData['testObjectiveID'],
            description=testData['description'],
            testSteps=testData['testSteps'],
            testerId=testData['testerID'])
        testRecord.save()
        if testRecord.id:
            return 200
        else:
            return 400
    except:
        return 400

def getTestPlansByproject(projectID):
    return TestPlan.objects.filter(project=projectID)

def getTestTestObjectivesByTestPlan(testObjectiveID):
    