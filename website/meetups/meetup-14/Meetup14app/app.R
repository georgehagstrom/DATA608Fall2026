#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(tidyverse)
library(thematic)
library(bslib)
library(ggplot2)



# Define UI for application that draws a histogram
ui <- fluidPage(
    theme=bs_theme(bootswatch = "darkly"),
    titlePanel("Old Faithful Geyser Data"),
    fluidRow(
        column(
            width = 3,
            div(style = "background-color:#f44336; color:white; padding:2px; border-radius:2px;",
                h4("Longest Eruption"),
                textOutput("maxEruption")
            )
        ),
        
        column(
            width = 3,
            div(style = "background-color:#f44336; color:white; padding:5px; border-radius:5px;",
                h4("Average Eruption"),
                textOutput("meanEruption")
            )
        )
        ,
        
        column(
            width = 3,
            div(style = "background-color:#4CAF50; color:white; padding:5px; border-radius:5px;",
                h4("Longest Waiting Time"),
                textOutput("maxWaiting")
            )
        ),
        
        
        column(
            width = 3,
            div(style = "background-color:#4CAF50; color:white; padding:5px; border-radius:5px;",
                h4("Average Waiting Time"),
                textOutput("meanWaiting")
            )
        )
    ),
    
    
    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            sliderInput("bins",
                        "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30)
        ),
        # Show a plot of the generated distribution
        mainPanel(
        tabsetPanel(
       tabPanel("Heatmap",plotOutput("heatmap")),
       tabPanel("Histogram",plotOutput("distPlot")),
       tabPanel("Description",p("Old faitful is a geyser in yellowstone that erupts periodically"))
        
       )
       )
      
    )
)


# Define server logic required to draw a histogram
server <- function(input, output) {
    thematic_shiny()
    
    output$maxEruption <- renderText({
        sprintf("%.2f minutes",max(faithful$eruptions))
    })
    
    output$meanEruption <- renderText({
        sprintf("%.2f minutes",mean(faithful$eruptions))
    })
    
    output$maxWaiting <- renderText({
        sprintf("%.2f minutes",max(faithful$waiting))
    })
    
        output$meanWaiting <- renderText({
            sprintf("%.2f minutes",mean(faithful$waiting))
                    })  
    
    output$distPlot <- renderPlot({
        # generate bins based on input$bins from ui.R
        x    <- faithful[, 2]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)

        # draw the histogram with the specified number of bins
        hist(x, breaks = bins, col = 'darkgray', border = 'white',
             xlab = 'Waiting time to next eruption (in mins)',
             main = 'Histogram of waiting times')
    })
    
    output$heatmap = renderPlot({ggplot(faithfuld, aes(x = waiting, y = eruptions, z = density)) +
            geom_raster(aes(fill = density)) +         
            geom_contour(color = "white") +            
            scale_fill_viridis_c() +                   
            labs(title = "2D Density Plot of Faithful Eruptions",
                 x = "Waiting Time (min)",
                 y = "Eruption Duration (min)",
                 fill = "Density") 
            })
}

# Run the application 
shinyApp(ui = ui, server = server)
