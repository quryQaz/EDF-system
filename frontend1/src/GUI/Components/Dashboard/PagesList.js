import Drivers from "GUI/Components/Dashboard/Pages/Drivers"
import Processes from "GUI/Components/Dashboard/Pages/Processes"
import Registry from "GUI/Components/Dashboard/Pages/Registry"
import Logs from "GUI/Components/Dashboard/Pages/Logs"
import Errors from "GUI/Components/Dashboard/Pages/Errors"
import Programs from "GUI/Components/Dashboard/Pages/Programs"
import Users from "GUI/Components/Dashboard/Pages/Users"
import {Console} from "GUI/Components/Dashboard/Pages/Console"
import {Alert} from "GUI/Components/Dashboard/Pages/Alert"

const driversPage = {
    id: 1,
    title: 'Drivers',
    component: Drivers
};
const processesPage = {
    id: 2,
    title: 'Processes',
    component: Processes
};
const registryPage = {
    id: 3,
    title: 'Registry',
    component: Registry
};
const logsPage = {
    id: 4,
    title: 'Logs',
    component: Logs
};
const errorsPage = {
    id: 5,
    title: 'Errors',
    component: Errors
};
const programsPage = {
    id: 6,
    title: 'Programs',
    component: Programs
};
const usersPage = {
    id: 7,
    title: 'Users',
    component: Users
};
const consolePage = {
    id: 8,
    title: 'Console',
    component: Console
};
const alertPage = {
    id: 9,
    title: 'Alert',
    component: Alert
};

export const getPages = () => {
    const pages = [
        driversPage,
        processesPage,
        registryPage,
        logsPage,
        errorsPage,
        programsPage,
        usersPage,
        consolePage,
        alertPage,
      ];
    return pages;
};
