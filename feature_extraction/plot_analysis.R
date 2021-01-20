df = read.csv(file="features.csv", header=TRUE)
library("dplyr")


library(ggplot2)
# Plot with all RTs and the mean for each face type
#png(file="plot.png",width=2000,height=2000, res=300)
df.mean_sd <- df %>% 
  group_by(condition) %>% 
  summarise(mean = mean(importance_height), sd = sd(importance_height))

ggplot(df, aes(condition, importance_height, color=condition)) +
  geom_jitter(width = 0.25, show.legend = FALSE)+
  geom_point(data = df.mean_sd, aes(condition, mean), colour = 'black', size = 4)+
  xlab("Input dataset")+
  #ylab("?")+
  theme_bw()+
  theme(text = element_text(size=18), axis.text.x = element_text(color = "black"), axis.text.y = element_text(color = "black"))+
  geom_errorbar(
    data = df.mean_sd,
    aes(condition, mean, ymin = mean - sd, ymax = mean + sd),
    colour = 'black',
    width = 0.3,
    size=0.7
  )
  #labs(title = "All RTs and the mean for each face type")+
  #geom_hline(yintercept=angryMean, linetype="dashed", color = "black")+
  #geom_hline(yintercept=neutralMean, linetype="dashed", color = "black")
#dev.off()