/*
Give the number of registrations by users from 'Group 1' in company 1.
*/
SELECT
    training.id AS training_id,
    TrainingLanguage(training.id, 1, 'title') AS training_title,
    COUNT(trainingsubscription.id) AS number_of_registrations
FROM
    training
        JOIN trainingsubscription ON training.id = trainingsubscription.idtraining
        JOIN user ON trainingsubscription.iduser = user.id
        JOIN userusergroup ON user.id = userusergroup.iduser
        JOIN usergroup ON userusergroup.idusergroup = usergroup.id
WHERE
    usergroup.name = 'Group 1'
  AND usergroup.idcompany = 1
  AND usergroup.disabled = 0
  AND user.disabled = 0
  AND trainingsubscription.disabled = 0
  AND training.disabled = 0
GROUP BY
    training.id
ORDER BY
    number_of_registrations DESC
LIMIT 10000;


/*
user_input = I want the number of trainings each day for all users over the past year indexed by email."
*/
SELECT 
        u.email,
        DATE(ts.subscribedate) AS training_date,
        COUNT(ts.id) AS training_count
    FROM 
        trainingsubscription ts
    JOIN 
        user u ON ts.iduser = u.id
    WHERE 
        ts.subscribedate >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    GROUP BY 
        u.email, DATE(ts.subscribedate)
    ORDER BY 
        u.email, training_date;

/*
user_input = "What percentage of registrations of each company?"
*/
SELECT 
    c.id AS company_id, 
    c.name AS company_name, 
    COUNT(ts.id) AS total_registrations,
    (COUNT(ts.id) * 100.0 / (SELECT COUNT(*) FROM trainingsubscription)) AS registration_percentage
FROM 
    trainingsubscription ts
JOIN 
    company c ON ts.idcompany = c.id
GROUP BY 
    c.id, c.name
ORDER BY 
    registration_percentage DESC;

/*Url Pie Char*/
https://www.quickchart.io/chart?c=%7B%0A%20%20%22type%22%3A%20%22outlabeledPie%22%2C%0A%20%20%22data%22%3A%20%7B%0A%20%20%20%20%22labels%22%3A%20%5B%22Mobile%22%2C%20%22Company%201%22%2C%20%22Company%202%22%2C%20%22Training%20Waiting%20List%22%2C%20%22Mobile%203%22%2C%20%22Teams%20Session%20Attendance%20Company%22%5D%2C%0A%20%20%20%20%22datasets%22%3A%20%5B%7B%0A%20%20%20%20%20%20%20%20%22backgroundColor%22%3A%20%5B%22%23FF3784%22%2C%20%22%2336A2EB%22%2C%20%22%234BC0C0%22%2C%20%22%23F77825%22%2C%20%22%239966FF%22%2C%20%22%23FFCE56%22%5D%2C%0A%20%20%20%20%20%20%20%20%22data%22%3A%20%5B77.2959%2C%2011.4796%2C%204.3367%2C%203.0612%2C%202.2959%2C%201.5306%5D%0A%20%20%20%20%7D%5D%0A%20%20%7D%2C%0A%20%20%22options%22%3A%20%7B%0A%20%20%20%20%22plugins%22%3A%20%7B%0A%20%20%20%20%20%20%22legend%22%3A%20false%2C%0A%20%20%20%20%20%20%22outlabels%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22text%22%3A%20%22%25l%20%25p%22%2C%0A%20%20%20%20%20%20%20%20%22color%22%3A%20%22white%22%2C%0A%20%20%20%20%20%20%20%20%22stretch%22%3A%2035%2C%0A%20%20%20%20%20%20%20%20%22font%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22resizable%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%22minSize%22%3A%2012%2C%0A%20%20%20%20%20%20%20%20%20%20%22maxSize%22%3A%2018%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D