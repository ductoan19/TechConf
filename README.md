## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:

| Azure Resource                 | Service Tier                | Monthly Cost |
| ------------                   | ------------                | ------------ |
| *Azure Postgres Database*      | Burstable                   | $19          |
| *Azure Service Bus*            | Basic                       | < $1         |
| *Azure web app*                | F1                          | 0            |
| *Azure function app*           | Y1                          | < $1         |
| *Azure application insight*    | Y1                          | < $1         |
| *Azure storage account*        | Standard                    | ~ $1         |


## Architecture Explanation
Why function & web app instead of VMs?
   => Scalabity & high availability are still supported (if need, but this case we don't need)
   => Easy to setup
   => No need much compute resource (<14 GB of RAM, < 4 CPU)

Why free tier os web app?
   => Small workload, in real project we will consider using higher service tiers
Why consumtion tier for function?
   => Small amount of consumtion, free first 400,000 GB-s and 1 milion executions per month
   => Nearly no cost for this exercise
Why Burstable tier of DB?
   => Same reason, our workload & storage consumption is not much
   => Choose the cheapest tier