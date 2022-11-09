To run crud api tests, on Jenkins, run the job: Popravka_behave_api

To run crud ui tests, on Jenkins, run the job: Popravka_behave

To run two tests together API and UI , run the job on Jenkins: Popravka
(the first will be UI. To change, go to settings JOB "Popravka" and change param: Build Steps)

Run tests with Allure report (command for terminal):
behave -f allure_behave.formatter:AllureFormatter -o results ./features

After passing the tests, you can create a report in the browser, run on terminal:
allure serve results

To create a folder in a project with reports (Allure report):
allure generate results

To save the history, transfer the history folder to the folder results

After re-running the tests and creating a folder in the project, you need to clear this folder to write new data(Allure report):
allure generate --clean results


