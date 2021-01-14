/**********************************************************
*	SQL Query & Function Example2
**********************************************************/
/**
-- Employees Table Columns
-- EMPLOYEE_ID
-- FIRST_NAME
-- LAST_NAME
-- EMAIL
-- PHONE_NUMBER
-- HIRE_DATE
-- JOB_ID
-- SALARY
-- COMMISSION_PCT
-- MANAGER_ID
-- DEPARTMENT_ID
**/

/**
--Departments Table Columns
--DEPARTMENT_ID
--DEPARTMENT_NAME
--MANAGER_ID
--LOCATION_ID
**/

/**
50번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하라
**/
select round(avg(salary), 0) 평균, max(salary) 최고, min(salary) 최저, count(*) 인원수 from employees where department_id = 50;




/**
각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하라.
**/
select department_id 부서번호, round(avg(salary), 0) 평균, max(salary) 최고, min(salary) 최저, count(*) 인원수 FROM employees group by department_id;





/**
각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하라.
**/
select department_id 부서번호, job_id 업무명, count(*) 인원수 From employees group by department_id, job_id order by department_id;




/**
같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하라.
**/
select job_id 업무, count(*) 인원수 from employees group by job_id having count(*) >= 4;




/**
각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하라.
**/
select department_id 부서번호, round(avg(salary), 0) 평균월급, sum(salary) 전체월급, max(salary) 최고월급, min(salary) 최저월급 from employees group by department_id order by 평균월급 DEsc;

/**
 부서번호, 부서명, 이름, 급여를 출력하라.
**/
select A.department_id 부서번호, B.department_name 부서명, first_name 이름, salary 급여 from employees A, departments B where A.department_id = B.department_id;

/**
이름이 adam인 사원의 부서명을 출력하라.
**/
select B.department_name 부서명 from employees A, departments B where A.department_id = B.department_id and A.first_name = 'Adam';
/**
employees테이블에 있는 employee_id와 manager_id를 이용하여 서로의 관계를 다음과 같이 출력하라
'smith'의 매니저는 'ford'이다.
**/
select B.first_name||'의 매니저는 '|| A.first_name||' 이다.' from employees A, employees B where A.employee_id = B.manager_id;


/**
adam의 직무와 같은 직무를 갖는 사람의 이름, 부서명, 급여, 직무를 출력하라.
**/
select a.first_name 이름, b.department_name 부서명, a.salary 급여, a.job_id 직무 from employees a, departments b where a.department_id = b.department_id and (job_id = (select c.job_id from employees c where c.first_name = 'Adam'));

/**
전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하라.
**/
select a.employee_id 사원번호, a.first_name 이름, b.department_name 부서명, a.hire_date 입사일, c.city 지역, a.salary 급여 from employees a, departments b, locations c where a.department_id = b.department_id and b.location_id = c.location_id and a.salary > (select avg(salary) from employees);

/**
50번 부서사람들 중에서 30번 부서의 사원과 같은 업무를 하는 사원의 사원번호, 이름, 부서명, 입사일을 출력하라.
**/
select a.department_id 사원번호, a.first_name 이름, b.department_name 부서명, a.hire_date 입사일 from employees a, departments b where a.department_id = b.department_id and a.department_id = 50 and job_id in (select job_id from employees where department_id = 30);

/**
급여가 30번 부서의 최고 급여보다 높은 사원의 사원번호, 이름, 급여를 출력하라.
**/
select employee_id 사원번호, first_name 이름, salary 급여 from employees where salary > (select max(salary) from employees where department_id = 30);