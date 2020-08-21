
DROP TABLE DEPARTMENT;
CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);
INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (1, 'IT Billing', 1 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (2, 'Engineering', 2 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (3, 'Finance', 7 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (4, 'Engineering', 3 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (5, 'Finance', 4 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (6, 'Engineering', 5 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (7, 'Finance', 6 );