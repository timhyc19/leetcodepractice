```
- On-call is a rotation system for engineers that are required when a service goes down. 

- Particularily at Ecobee, there are dozens of data pipelines that process thousands of data points and requests / second, making it easy for the software to error out

- One of my main on-call errors was fixing a data pipeline failing due to high latency spikes. Because GCP has poor cold-start times, batching services that went down for a bit received too high of a threshold of data points too suddenly. To fix this, we simply increased the num workers (instances) for this pipeline, which minimized latency. 

- Naturally, processing the amount of data points exceeded the l;latency threshold, because as more consumers buy thermostats, the number of requests increases. 

- Other ways to have solved the problem could have been keeping some instances "warm" (ready to handle requests), or more long term solutions would be writing the pipelines in more fast processing languages like Golang. 
```